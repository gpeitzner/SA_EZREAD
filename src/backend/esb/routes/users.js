var express = require("express");
var router = express.Router();
const axios = require("axios").default;
const host = process.env.HOST_URL || "localhost";

/**Signup users */
router.post("/signup", function (req, res, next) {
	axios
		.post(`http://${host}:5002/users`, req.body)
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

/**Login users */
router.post("/login", function (req, res, next) {
	axios
		.post(`http://${host}:5000/`, req.body)
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

module.exports = router;
