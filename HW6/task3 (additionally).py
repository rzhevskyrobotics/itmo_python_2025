import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from torch.utils.data import TensorDataset, DataLoader
import torch
import torch.nn as nn
import torch.optim as optim

# Загружаем данные
data = pd.read_csv('data.csv')

# Удаляем столбец с названием дорожки (filename) и выделяем столбец label
data = data.drop(columns=['filename'])
labels = data['label']
features = data.drop(columns=['label'])

# Кодируем названия жанров в числа
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Нормализуем признаки
scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

# Разбиваем данные на тренировочную и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(scaled_features, encoded_labels, test_size=0.2, random_state=42)

# Преобразуем данные в формат PyTorch
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
X_test_tensor = torch.tensor(X_test, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)
y_test_tensor = torch.tensor(y_test, dtype=torch.long)

train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
test_dataset = TensorDataset(X_test_tensor, y_test_tensor)

train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)
test_loader = DataLoader(test_dataset, batch_size=64, shuffle=False)

# Определяем архитектуру нейронной сети
class MusicGenreClassifier(nn.Module):
    def __init__(self, input_size, num_classes):
        super(MusicGenreClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, 256)
        self.fc2 = nn.Linear(256, 128)
        self.fc3 = nn.Linear(128, 64)
        self.fc4 = nn.Linear(64, 32)
        self.fc5 = nn.Linear(32, 16)
        self.fc6 = nn.Linear(16, num_classes)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        x = torch.relu(self.fc5(x))
        x = torch.softmax(self.fc6(x), dim=1)
        return x

# Инициализируем модель, функции потерь и оптимизатора
input_size = X_train.shape[1]
num_classes = len(np.unique(encoded_labels))

model = MusicGenreClassifier(input_size, num_classes)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Обучаем модель
num_epochs = 20
for epoch in range(num_epochs):
    model.train()
    running_loss = 0.0
    correct = 0
    total = 0

    for inputs, labels in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    print(f'Эпоха [{epoch+1}/{num_epochs}], Потери: {running_loss:.4f}, Точность: {accuracy:.2f}%')

# Проверяем модель на тестовой выборке
model.eval()
correct = 0
total = 0
with torch.no_grad():
    for inputs, labels in test_loader:
        outputs = model(inputs)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

test_accuracy = 100 * correct / total
print(f'Точность на тестовой выборке: {test_accuracy:.2f}%')

# Проверяем предсказания модели на первом элементе тестовой выборки
first_test_input = X_test_tensor[0].unsqueeze(0)
true_label = y_test_tensor[0].item()
model.eval()
with torch.no_grad():
    output = model(first_test_input)
    _, predicted_label = torch.max(output.data, 1)
    predicted_label = predicted_label.item()

print(f'Истинный жанр: {label_encoder.inverse_transform([true_label])[0]}')
print(f'Предсказанный жанр: {label_encoder.inverse_transform([predicted_label])[0]}')