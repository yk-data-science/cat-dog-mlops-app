# Cat-Dog MLops App - External Design (with Confidence Scores)

## 1. Functional Requirements

| Feature                               | Description                                                | Priority |
|-------------------------------------|------------------------------------------------------------|----------|
| Image Upload                        | Users can upload one image by drag & drop or file select. | High     |
| Classification Results with Confidence Scores | Display classification result with probabilities for each class (e.g., Dog: 87%, Cat: 13%). | High     |
| Result History                      | Show uploaded image alongside classification result and probabilities. | Medium   |
| Error Handling                     | Notify user of invalid file types or upload failures.     | Medium   |

---

## 2. User Interface Design

### 2.1 Main Screen

- **Upload Area:**  
  Drag & drop or click to select image files.

- **Result Display:**  
  - Show the uploaded image.  
  - Show class probabilities, for example:  
    - Dog: 87%  
    - Cat: 13%  
  - Highlight the most probable class as the classification result.

- **Reset Button:**  
  Clear current image and result to upload a new one.

---

## 3. Data Flow

1. User uploads an image via frontend.  
2. Frontend sends the image to the backend API.  
3. Backend preprocesses the image and runs the classification model.  
4. Backend returns detailed prediction scores, e.g.:  
   `{ "dog": 0.87, "cat": 0.13 }`.  
5. Frontend displays the result with the uploaded image and percentage scores.

---

## 4. Technical Details

| Aspect            | Details                                                   |
|-------------------|-----------------------------------------------------------|
| API Response Format| JSON object with class probabilities, e.g.:  
`{ "dog": 0.87, "cat": 0.13 }`                             |
| Frontend Display  | Show probabilities as percentages with clear labels. Highlight the top class.|

---

## 5. API Example

**POST** `/classify-image`

### Request

- Form-data or JSON containing the image file.

### Response

```json
{
  "predictions": {
    "dog": 0.87,
    "cat": 0.13
  },
  "top_class": "dog"
}
