<template>
  <div class="container" style="max-width: 600px">
    <!-- Heading -->
    <h2 class="text-center mt-5">Todo App</h2>

    <!-- Input -->
    <div class="d-flex mt-5">
      <input
        type="text"
        v-model="task"
        placeholder="Enter task"
        class="w-100 form-control"
      />
      <button class="btn btn-warning rounded-0" @click="submitTask">
        SUBMIT
      </button>
      <button v-on:click.prevent="post">submitTask</button>
    </div>

    <!-- Task table -->
    <table class="table table-bordered mt-5">
      <thead>
        <tr>
          <th scope="col">Task</th>
          <th scope="col" style="width: 120px">Status</th>
          <th scope="col" class="text-center">#</th>
          <th scope="col" class="text-center">#</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(task, index) in tasks" :key="index">
          <td>
            <span :class="{ 'line-through': task.status === 'finished' }">
              {{ task.name }}
            </span>
          </td>
          <td>
            <span
              class="pointer noselect"
              @click="changeStatus(index)"
              :class="{
                'text-danger': task.status === 'to-do',
                'text-success': task.status === 'finished',
                'text-warning': task.status === 'in-progress',
              }"
            >
              {{ capitalizeFirstChar(task.status) }}
            </span>
          </td>
          <td class="text-center">
            <div @click="deleteTask(index)">
              <span class="fa fa-trash pointer"></span>
            </div>
          </td>
          <td class="text-center">
            <div @click="editTask(index)">
              <p class="fa fa-pen pointer"></p>
            </div>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  name: "todoapp",
  props: {
    msg: String,
  },
  data() {
    return {
      task: "",
      editedTask: null,
      statuses: ["to-do", "in-progress", "finished"],
      /* Status could be: 'to-do' / 'in-progress' / 'finished' */
      tasks: [
        {
          index: 1,
          name: "buy vegetables.",
          status: "to-do",
        },
        {
          index: 2,
          name: "study for 1 hour.",
          status: "in-progress",
        },
        {
          index: 3,
          name: "sleep.",
          status: "finished",
        },
      ],
    };
  },
  methods: {
      addItem: function() {
        this.tasks.push({
         index: this.tasks.length + 1,
         name: this.task,
         completed: false,
       });
        this.task = '';
     },
      removeItem: function (taskindex) {
        this.tasks = this.tasks.filter((task) => newtask.index!== taskindex);
     }, 
      addTodo() {
        if (this.newtask.trim().length == 0){
          return
    }
        const path = this.baseUrl;
        var newEntry = {
         'title': this.newtask,
         'status': false,
         'due': 0,
         'editing': false
        }
        Vue.axios.post(path, newEntry)
          .then(response => this.indexFortask = response.data.index)
          .then(this.todos.push(newEntry))
        this.newtask=''
        this.indexFortask++
              
    },
      removeTodo(index) {
        this.tasks.splice(index, 1)
        const path = this.baseUrl + "/" + index
        Vue.axios.delete(path)
    },
      editTodo(task) {
        todo.editing = true
     },
      updateTodo(task, index) {
        const path = this.baseUrl + "/" + index
        Vue.axios.put(path, {'title': task.title})
    },
      doneEdit(task, index) {
        this.updateTodo(todo, index);
        todo.editing = false
    }, 
      updateStatus(task, index) {
        const path = this.baseUrl + "/" + index + "/check"
        Vue.axios.put(path, {'status': !task.status}) // i think it takes the value before changing so i NOT it
    }
      
    }
 };    
</script>

<style scoped>
.pointer {
  cursor: pointer;
}
.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Old versions of Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome, Edge, Opera and Firefox */
}
.line-through {
  text-decoration: line-through;
}
</style>
