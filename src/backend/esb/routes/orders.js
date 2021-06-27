var express = require("express");
var router = express.Router();
const axios = require("axios").default;
const host = process.env.HOST_URL || "localhost";

/** GET orders listing. */
router.get("/", function (req, res, next) {
	axios
		.get(`http://${host}:5013/ordenes`, { data: req.body })
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

/** POST orders. */
router.post("/", function (req, res, next) {
	axios
		.post(`http://${host}:5010/ordenes`, req.body)
		.then((response) => {
			res.json(response.data);
		})
		.then((error) => {
			res.status(400).json(error);
		});
});

/** PUT orders. */
router.put("/", function (req, res, next) {
	axios
		.put(`http://${host}:5011/ordenes`, req.body)
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

/** DELETE orders. */
router.delete("/", function (req, res, next) {
	axios
		.delete(`http://${host}:5012/ordenes`, { data: req.body })
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

module.exports = router;
