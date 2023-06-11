// static/js/sanitizeNames.js
function sanitizeName(name) {
  var commonWords = ["the", "a", "an", "of", "and", "in", "is", "to", "for", "with", "on", "by", "as", "at", "from"];
  var titleWords = ["King", "Queen", "Prince", "Princess", "Lord", "Lady"];

  var words = name.toLowerCase().split(" ");
  var sanitizedWords = [];

  for (var i = 0; i < words.length; i++) {
    var word = words[i];
    if (!commonWords.includes(word) && !titleWords.includes(word)) {
      sanitizedWords.push(word);
    }
  }

  return sanitizedWords.join(" ");
}
