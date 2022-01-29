<template>
    <br>
	<h1>NLP Vue Assignment 1</h1>
    <h2>To-dos</h2>
    <br>
	<form @submit.prevent="create_todo()">
		<label>Add a task </label>
		<input
			v-model="input"
			name="input"
			autocomplete="off"
		>
		<button>Click me</button>
        <br>
	</form>
    <div id="temp">
        <ul>
            <li
                v-for="(todo, index) in todos"
                :key="index"
            >
                <input v-if = "todo.edit" v-model = "todo.content"
                @blur= "todo.edit = false; $emit('update')"
                @keyup.enter = "todo.edit=false; $emit('update')">
                    <div v-else>
                        <span
                            :class="{ done: todo.done }"
                            @click="todo.edit = true;"
                        >{{ todo.content + " " }}</span>
                    <button id="removal" @click="remove(index)">Remove</button>
                    </div>
            <br>
            </li>
        </ul>
    </div>
	<h4 v-if="todos.length === 0">Empty list.</h4>
    <h3> (click tasks to edit, enter to save) </h3>
    <a href="https://github.com/decdod/nlp-class/blob/dev/src/views/Todo.vue">Todo.vue</a>
</template>

<script>
import { ref } from 'vue';

export default {
  name: 'Todo',
  setup() {
    const input = ref('');

    // const todosData = JSON.parse(localStorage.getItem('todos')) || defaultData;
    // const todosData =
    const todos = ref([]);
    if (!todos.value.length) {
      todos.value.push({
        content: 'Finish the assignment ',
      });
      todos.value.push({
        content: 'Remember to submit the assignment ',
      });
    }
    const create_todo = () => {
      if (input.value) {
        todos.value.push({
          content: input.value,
        });
        input.value = '';
      }
    }

    const remove = (index) => {
      todos.value.splice(index, 1);
    }
    return {
      todos,
      create_todo,
      remove,
      input,
    };
  },
};
</script>

<style>
#temp {
  display: inline-block;
  text-align: left;
}
#removal {
  text-align: left;
}
</style>
