const seedData = require('../server/seedData.js');

const course3 = seedData.courses.find(c => c.id === 3 || c.slug === 'reasoning');
console.log('Course 3:', course3);

const modules = seedData.modules.filter(m => m.course_id === 3);
console.log('Modules for course 3:', modules);

const topics = seedData.topics.filter(t => t.course_id === 3);
console.log(`Topics for course 3 (${topics.length}):`);
topics.forEach(t => console.log(`  ID: ${t.id}, Title: ${t.title}, Module: ${t.module_id}, Order: ${t.order_index}`));
