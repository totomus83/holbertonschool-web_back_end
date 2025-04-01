export default function cleanSet(set, string) {
  if (string === '') {
    return '';
  }
  const result = Array.from(set)
    .filter((item) => item.startsWith(string))
    .map((item) => item.slice(string.length));

  return result.join('-');
}