# apple-banana-orange-detector


##  YOLOv10 Fruit Detector

The **YOLOv10 Fruit Detector** is a high-performance deep learning system designed for the real-time identification and classification of various fruit types. By utilizing the latest **End-to-End** object detection architecture, the system achieves superior inference speeds by eliminating traditional post-processing bottlenecks.

###  Key Features

* **NMS-Free Inference:** High-speed processing enabled by a consistent dual-assignment strategy, removing the need for Non-Maximum Suppression (NMS).
* **High-Precision Localization:** Accurately identifies overlapping fruits and small objects (like berries or grapes) in cluttered scenes.
* **Real-Time Counting:** Integrated logic to tally total fruit counts per class for inventory or harvest analysis.
* **Hardware Efficiency:** Optimized for low-latency performance on both high-end GPUs and resource-constrained edge devices.
* **Visual Overlays:** Renders sleek bounding boxes with dynamic class labels and confidence scores.

---

### 🛠 Tech Stack & Methodology

The project follows a modern ML pipeline centered on architectural efficiency:

| Phase | Technology | Description |
| --- | --- | --- |
| **Data Prep** | Python / XML-to-YOLO | Custom scripts to migrate legacy XML annotations to standardized YOLO formats. |
| **Model** | **YOLOv10** | Employs a lightweight classification head and spatial-channel decoupled downsampling. |
| **Training** | PyTorch / Ultralytics | Uses dual label assignment (1-to-1 and 1-to-many) for rich supervision. |
| **Inference** | ONNX / TensorRT | Exportable to optimized formats for sub-millisecond deployment. |

---

###  Training & Performance

* **Dual-Assignment Strategy:** During training, the model uses a "one-to-many" head for rich gradient information and a "one-to-one" head for "NMS-free" deployment.
* **Robust Augmentation:** Utilizes Mosaic, Mixup, and Color Jittering to ensure the model remains accurate under diverse lighting and background conditions.
* **Optimization:** Leverages **Partial Self-Attention (PSA)** modules to capture global context without the heavy computational cost of standard transformers.

---

###  Use Cases

* **Smart Agriculture:** Automated ripeness detection and yield estimation in orchards.
* **Retail Tech:** AI-powered checkout scales that identify produce without manual entry.
* **Quality Control:** Sorting systems that filter out bruised or damaged fruit on conveyor belts.

---

###  Notes

* **Resolution:** 640px is the standard training size; increasing to 1280px can improve detection for smaller fruits but increases latency.
* **Confidence Tuning:** Because YOLOv10 is NMS-free, fine-tuning the `conf` threshold is the primary way to balance precision and recall.
