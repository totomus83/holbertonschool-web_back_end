import kue from 'kue';

const queue = kue.createQueue();

/**
 * Job data object
 */
const jobData = {
  phoneNumber: '123456789',
  message: 'Hello from Holberton School',
};

/**
 * Create job in queue
 */
const job = queue.create('push_notification_code', jobData);

/**
 * When job is created successfully
 */
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

/**
 * When job is completed
 */
job.on('complete', () => {
  console.log('Notification job completed');
});

/**
 * When job fails
 */
job.on('failed', () => {
  console.log('Notification job failed');
});

/**
 * Save job
 */
job.save((err) => {
  if (err) {
    console.log('Error creating job');
  }
});