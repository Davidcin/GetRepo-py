# GetRepo-py

---
**GetRepo-py** is a command line client that queries **GitHub API** and searches repositories by given arguments.<br>
It is a *test* task for the Back-End Developer role vacancy in a company **Noxtton**.
---
![terminal]( https://i.ibb.co/ftJrSGJ/uploadbb.png)

---
### I completed every task (including bonus ones).

### tasks:

1. The client should accept a search string, query GitHub API for repositories and display the results.<br>
2. In addition to the search word, the client should accept two optional parameters.<br>
     * Ignore Parameter will ignore repositories, where the name of the repository includes the provided string.
     * Sort Parameter will sort results by repository name in Ascending or Descending order.
3. Solution needs to be documented in Markdown format.<br>
4. Add unit tests to your solution.<br>
5. Log all search requests in a separate log file.<br>
6. Provide a Docker file to build your solution as a Docker Image. Include building and running instructions in the documentation.

---
### I also added some **features** (to get bonus points for creativity :smiley: ):
1. You can specify a programming language to query repos by it.<br>
2. Additional sorts. sort and order are separated.<br>
   * There are 4 sort options: by number of stars, forks, help-wanted-issues and last updated date.<br> 
   * And you can choose to sort in ascending or descending order.
3. You can specify how many results you want to get.
4. Colored terminal to make it prettier/more visible.
5. Before adding unit tests I accessed GitHub API with Postman and got specific (static) urls and test json data that is stored in the jsonTest folder. I tested my function with that.
6. In addition to a log file that is fully dynamic, you can choose to save results to the json file, that is stored in the SavedJSON folder.
---
#### I have used following libraries:
```
requests
json
colorama
logging
unittest
```
----
## Docker

At first build docker image:<br>
`docker build -t getrepo .`<br>
then run container:<br>
`docker run -t -i getrepo`