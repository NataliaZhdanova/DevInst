import express from "express";
import router from "./routes/index.js";

const app = express();
const port = 9000;

app.use(express.json());

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
  });


app.use("/", router);



app.use((req, res) => {
    res.status(404).json({ error: "Route not found" });
  });
  

app.use((err, req, res, next) => {
    console.error(err);
    res.status(500).json({ error: "Internal Server Error" });
  });
