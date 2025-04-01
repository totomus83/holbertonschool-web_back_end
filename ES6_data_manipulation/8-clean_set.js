export default function cleanSet(set, startString) {
  if (startString === '') {
    return '';
  }
  const result = Array.from(set)
    .filter((item) => item.startsWith(startString))
    .map((item) => item.slice(startString.length));

  return result.join('-');
}
