import redis from 'redis';
import { promisify } from 'util';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.message);
});

// Convert callback-based get into Promise
const getAsync = promisify(client.get).bind(client);

/**
 * Set value in Redis (still callback-based as required by task 2/3 progression)
 */
function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

/**
 * Async version using await
 */
async function displaySchoolValue(schoolName) {
  const value = await getAsync(schoolName);
  console.log(value);
}

/* Calls required by the task */
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');