const express = require('express');
const bodyParser = require('body-parser');
const shortid = require('shortid');
const app = express();
const port = 5000;

app.use(bodyParser.json());

// Store short URLs (in-memory database)
let urls = {};

app.post('/api/shorten', (req, res) => {
  const { url } = req.body;
  const id = shortid.generate();
  urls[id] = url;
  const shortUrl = `http://localhost:${port}/api/${id}`;
  res.json({ shortUrl });
});

app.get('/api/:id', (req, res) => {
  const id = req.params.id;
  const originalUrl = urls[id];
  if (originalUrl) {
    res.redirect(originalUrl);
  } else {
    res.status(404).send('URL not found');
  }
});

app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
