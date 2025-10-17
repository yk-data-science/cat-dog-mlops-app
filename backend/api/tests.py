import os
from django.test import TestCase
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from django.core.files.uploadedfile import SimpleUploadedFile


class DoubleApiTests(TestCase):
    def test_double_value(self):
        response = self.client.post(
            '/api/double/',
            data=json.dumps({'number': 5}),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['result'], 10)

# class PredictApiTests(TestCase):
#     def test_predict_api(self):
#         # Simulate a file upload
#         img = SimpleUploadedFile("test.jpg", b"dummydata", content_type="image/jpeg")
#         response = self.client.post("/api/predict/", {"file": img})
        
#         self.assertEqual(response.status_code, 200)
#         data = json.loads(response.content)
#         self.assertIn("result", data)

class PredictApiTests(TestCase):
    def test_predict_api(self):
        img_path = os.path.join(os.path.dirname(__file__), "../tests/free_cat2.jpg")
        with open(img_path, "rb") as f:
            img = SimpleUploadedFile("free_cat2.jpg", f.read(), content_type="image/jpeg")

        response = self.client.post("/api/predict/", {"file": img})
        self.assertEqual(response.status_code, 200)

        # Optional: check if prediction key exists
        self.assertIn("prediction", response.json())
        print("Predicted:", response.json()["prediction"])
    