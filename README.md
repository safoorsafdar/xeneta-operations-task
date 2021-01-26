# Practical section
## Running the API service

Start from the root folder.

### 1. Install prerequisites
* Docker
* Doker Compose

### 2. Run the application
```
docker-compose up --build --force-recreate
```
Note: it will also start the database service for the rates application with default defined `.sql` file from `db` folder.

### 3. Tear Down
```
docker-compose down --volume
```

The API should now be running on [http://localhost:3000](http://localhost:3000).

### 3. Test the application

Get average rates between ports:
```
curl "http://127.0.0.1:3000/rates?date_from=2016-01-01&date_to=2016-01-31&orig_code=CNGGZ&dest_code=EETLL"
```

The output should be something like this:
```
{
   "rates" : [
      {
         "count" : 3,
         "day" : "2016-01-31",
         "price" : 1154.33333333333
      },
      {
         "count" : 3,
         "day" : "2016-01-30",
         "price" : 1154.33333333333
      },
      ...
   ]
}
```

# Theoretical section
In this section we are seeking high-level answers, use a maximum of couple of paragraphs to answer the questions.

## Extended service

Imagine that for providing data to fuel this service, you need to receive and insert big batches of new prices, ranging within tens of thousands of items, conforming to a similar format. Each batch of items needs to be processed together, either all items go in, or none of them does.

Both the incoming data updates and requests for data can be highly sporadic - there might be large periods without much activity, followed by periods of heavy activity.

High availability is a strict requirement from the customers.

* How would you design the system?
### Single Point of failure
One of the foundations of high availability is eliminating single points of failure by achieving redundancy on all levels. A single point of failure is any component of the system which would cause the rest of the system to fail if that individual component failed. We can use 2N+1 model, which provides the same level of availability and redundancy as 2N with the addition of another component for improved protection. 

 ### Data Backup and recovery
A high availablity system mush have sound data protection and DR plans. An absolute must is to have proper backups. Another critical thing is the ability to recover in case of a data loss quickly, corruption, or complete storage failure.

### Failover with failure detection
In a highly available, redundant IT infrastructure, the system needs to instantly redirect requests to a backup system in case of a failure. This is called failover. Early failure detections are essential for improving failover times and ensuring maximum systems availability.

### Observability
Observability is tooling or  techinal solution that allows teams to actively debug their system. Observability is based on exploring properties and patterns not defined in advance. Good observability can contain monitoring and logging of the system.

### Chaos Engineering
Chaos Engineering is the discipline of experimenting on a system in order to build confidence in the system’s capability to withstand turbulent conditions in production.

* How would you set up monitoring to identify bottlenecks as the load grows?
> The most common strategy for failure monitoring and detection on redundant systems is this top-to-bottom technique. Implementing the observability can help to track bottlenecks in the systems by collecting system logs into i.e. ELK stack and monitoring the system on all layeres such as application, database and infrasturcture.
* How can those bottlenecks be addressed in the future?
> Addressing bottleneck issues usually results in returning the system to operable performance levels; however, fixing bottleneck issues requires first identifying the underperforming component. Observability and Chaos engineering can help to identify some bottlenecks in advance. Bottleneck resolution would depends on issue itself.

Provide a high-level diagram, along with a paragraphs describing the choices you've made and what factors do you need to take into consideration.

## Additional questions

Here are a few possible scenarios where the system requirements change or the new functionality is required:

1. The batch updates have started to become very large, but the requirements for their processing time are strict.
> We can utilize pg_dump over COPY to process large data in various chunk and asynchronous execution to decrease over execution time and have queue mechanism to deal with task execution.

2. Code updates need to be pushed out frequently. This needs to be done without the risk of stopping a data update already being processed, nor a data response being lost.
> We can have various deployment stratagey in place to deploy new releases such as Blue/Green to insure that new release are functional before deleting old release or old running application.

3. For development and staging purposes, you need to start up a number of scaled-down versions of the system.
> If we are on containerize environment or monolith environment, we can have IAC in place to replicate application and infrastructure for various environment. and to ensure each environment have similar database schema, we can have migration and dummy data seeds to have up to date database schema with data.

Please address *at least* one of the situations. Please describe:

- Which parts of the system are the bottlenecks or problems that might make it incompatible with the new requirements?
> Bulk updates of database may become bottleneck when the system grows, for HA/Active/Passive DB cluster, replication and availability of data across nodes may become troublant. 
- How would you restructure and scale the system to address those?
