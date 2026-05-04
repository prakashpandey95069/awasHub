const express = require("express");
const axios = require("axios");
const cors = require("cors");

const app = express();
app.use(express.json());
app.use(cors());

app.post("/predict", async (req, res) => {
    try {

        const response = await axios.post("http://127.0.0.1:5001/predict", req.body);
        res.json(response.data);
    } catch (error) {
        if (error.response) {
            console.error("ML Service error response status:", error.response.status);
            return res.status(error.response.status).json(error.response.data);
        }
        console.error("ML Service connection error:", error.message);
        res.status(500).json({ error: "ML Service connect nahi ho saki" });
    }
});

app.listen(5000, () => {
    console.log("Node.js server running on port 5000");
});