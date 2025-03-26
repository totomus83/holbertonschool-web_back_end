export default function appendToEachArrayValue(array, appendString) {
  let idx = 0;
  const appendedarray = [];
  for (const value of array) {
    appendedarray[idx] = appendString + value;
    idx += 1;
  }

  return appendedarray;
}
