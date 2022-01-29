import { createWebHistory, createRouter } from 'vue-router';
import Home from '../views/Home.vue';
import NLP from '../views/NLP.vue';
import NLP_Code from '../views/NLP_Code.vue';
import Todo from '../views/Todo.vue';
import Highlighting from '../views/Highlighting.vue';

const routes = [
  {
    path: '/',
    redirect: { name: 'Home' },
  },
  {
    path: '/nlp-class/',
    name: 'Home',
    component: Home,
  },
  {
    path: '/nlp-class/todo',
    name: 'Todo',
    component: Todo,
  },
  {
    path: '/nlp-class/nlp',
    name: 'NLP',
    component: NLP,
  },
  {
    path: '/nlp-class/nlp-code',
    name: 'NLP_Code',
    component: NLP_Code,
  },
  {
    path: '/nlp-class/highlighting',
    name: 'Highlighting',
    component: Highlighting,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
