import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

from data import generate_sensor_data

X, y = generate_sensor_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

joblib.dump(model, "maintenance_model.pkl")
print("model kaydedildi: maintenance_model.pkl")
