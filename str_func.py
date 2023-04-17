function getCapitals(text) {
if (text == text.toLowerCase()) {
  return []
}
 
return [text.match(/[A-Z]/g).join(' , ')]
}
