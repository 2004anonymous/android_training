const express = require("express");
const multer = require("multer");
const path = require("path");
const axios = require("axios");
const FormData = require("form-data");
const cors = require("cors");

const app = express();
app.use(express.json());
const port = 4000;
app.use(cors());
const storage = multer.memoryStorage();
const upload = multer({ storage: storage });

app.use(express.static(path.join(__dirname, "public")));

app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "index.html"));
});

app.get("/entries", (req, res) => {
  res.sendFile(path.join(__dirname, "dashboard.html"));
});

app.post("/upload", upload.single("qp"), async (req, res) => {
  const result = { success: false, message: "Uploading failed!" };

  const { department, subject, semester, year } = req.body;
  const fileData = req.file.buffer;

  try {
    const formData = new FormData();
    formData.append("file", fileData, {
      filename: req.file.originalname,
      contentType: req.file.mimetype,
    });
    formData.append("year", year);
    formData.append("sem", semester);
    formData.append("dept", department);
    formData.append("sub", subject);

    await axios.post("http://127.0.0.1:8000/paper/upload", formData, {
      headers: {
        ...formData.getHeaders(),
      },
    });

    result.success = true;
    result.message = "File uploaded successfully!";
  } catch (error) {
    console.error("Error:", error);
  }

  res.json(result);
});

app.get("/get-entries", async (req, res) => {
  try {
    const fastApiResponse = await axios.get("http://127.0.0.1:8000/paper/find");
    const entries = fastApiResponse.data;
    res.json(entries);
  } catch (error) {
    console.error("Error fetching entries from FastAPI:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.delete("/paper/delete/:id", async (req, res) => {
  const entryId = req.params.id;

  try {
    await axios.delete(`http://127.0.0.1:8000/paper/delete/${entryId}`);
    res.json({ success: true, message: "Entry deleted successfully!" });
  } catch (error) {
    console.error("Error deleting entry from FastAPI:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});


app.put("/paper/edit/:id", async (req, res) => {
  const entryId = req.params.id;
  const { sem, year, sub, dept } = req.body;

  try {
    console.log("Received data:", { entryId, sem, year, sub, dept });

    const updatedData = {
      id: entryId,
      year: year,
      sem: sem,
      dept: dept,
      sub: sub,
    };

    await axios.put(`http://127.0.0.1:8000/paper/edit/${entryId}`, updatedData, {
      headers: {
        'Content-Type': 'application/json',
      },
    });

    res.json({ success: true, message: "Entry updated successfully!" });
  } catch (error) {
    console.error("Error updating entry from FastAPI:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});

app.post("/dashboard-data", async (req, res) => {
  const jsonData = req.body;

  try {
    // Process the jsonData here
    console.log("Received JSON data from dashboard:", jsonData);

    // Perform any necessary operations with the jsonData

    res.json({ success: true, message: "JSON data received successfully!" });
  } catch (error) {
    console.error("Error processing JSON data:", error);
    res.status(500).json({ error: "Internal Server Error" });
  }
});



app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
