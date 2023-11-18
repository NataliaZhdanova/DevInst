import express from "express";
const router = express.Router();

router.get("/", function(req, res, next) {
	res.send("Responding with a resource");
});

export default router;