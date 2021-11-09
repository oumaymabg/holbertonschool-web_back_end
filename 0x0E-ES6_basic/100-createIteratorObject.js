export default function createIteratorObject(report) {
    const workers = [];
    /* eslint-disable no-unused-vars Iterating through report objects*/
    for (const [department, employees] of Object.entries(report.allEmployees)) {
      for (const employe of employees) {
        workers.push(employe);
      }
    }
    /* eslint-enable no-unused-vars Iterating through report objects*/
  
    return workers;
  }