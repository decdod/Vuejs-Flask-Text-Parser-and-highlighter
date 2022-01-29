<template>
  <div>
    <router-link to="/nlp-class">Home</router-link> |
    <router-link to="/nlp-class/todo">Todo</router-link> |
    <router-link to="/nlp-class/nlp">NLP</router-link> |
    <router-link to="/nlp-class/nlp-code">NLP-Code</router-link> |
    <router-link to="/nlp-class/highlighting">Highlighting</router-link>
  </div>
  <router-view />

</template>

<script>

export default {
  name: 'App',
  components: {
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
