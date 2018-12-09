
● We have electricity consumption data that is needed by one of our algorithms, with the output being served to other internal services. We have provided some sample data that shows the structure, and will give insight into how it should be stored.

● One of the consumers of the API will be an internal algorithm that will process the raw data and match intervals with buyers and sellers. It is possible that this algorithm runs more than once for the same set of raw data, with differing outputs.

● The raw data consists of interval readings keyed by icp_id. The algorithm will output data that will also need to be stored, which has similar columns but will also need an additional buyer/seller identifier.
Your tasks

1. Design an API that...

● Given an icp_id, and date range, returns raw data for the algorithm

● Given an icp_id, date range and buyer/seller, returns aggregated algorithm output data

● Given an icp_id, return paginated aggregated algorithm output data

● Given a date range, returns algorithm output data by key

2. For the database, provide a schema and/or migrations as to how you would build the database.
Your answers do not need to be super detailed, we are mostly looking for how you approach the problem and what solution(s) you come up with, and their pros/cons.


Sample data

The raw electricity consumption data is structured as follows. You should assume there could be hundreds of thousands of meters (i.e. ICPs), 48 half-hourly readings per day, and 14 days of readings to be processed at a time.

read_timestamp,interval_read,energy_flow_direction,icp_id
2018-06-14 00:30:00+12,1.343,X,33
2018-06-17 13:00:00+12,1.013,X,33
2018-06-23 09:00:00+12,1.336,X,33
2018-06-23 11:00:00+12,1.203,X,33
2018-06-21 07:30:00+12,2.569,X,33



The algorithm returns data like this:

icp_id, matched_amount, read_date, read_time, publish_datetime,buyer_seller

101, "0.0000", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.057601+12", “buyer”
100, "0.0040", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.057658+12", “seller”
102, "0.0010", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.057693+12", “buyer”
104, "0.0030", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.057728+12", “buyer”
105, "0.0010", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.057759+12", “buyer”
107, "0.0160", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.05779+12", “buyer”
108, "0.0050", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.057819+12", “seller”
109, "0.0180", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.05785+12", “buyer”
110, "0.0010", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.05788+12", “buyer”
113, "0.0000", "2018-06-13", "00:00:00", "2018-06-27 16:39:36.05791+12", “buyer”
