var express = require("express");
var router = express.Router();

/** GET orders listing. */
router.get("/", function (req, res, next) {
	res.send("orders");
});

module.exports = router;
