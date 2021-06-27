var express = require("express");
var router = express.Router();
const axios = require("axios").default;
const host = process.env.HOST_URL || "localhost";

/**GET books. */
router.get("/", function (req, res, next) {
	axios
		.get(`http://${host}:5009/libros`)
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

/**POST books. */
router.post("/", function (req, res, next) {
	axios
		.post(`http://${host}:5006/libros/crear`)
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

/**PUT books. */
router.put("/", function (req, res, next) {
	axios
		.put(`http://${host}:5007/libros/editar`)
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

/**DELETE books. */
router.delete("/:id", function (req, res, next) {
	axios
		.delete(`http://${host}:/libros/eliminar?id=` + req.params.id)
		.then((response) => {
			res.json(response.data);
		})
		.catch((error) => {
			res.status(400).json(error);
		});
});

module.exports = router;
