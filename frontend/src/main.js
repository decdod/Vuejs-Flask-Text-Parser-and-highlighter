import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import Highlight from './components/Highlight.vue'

const app = createApp(App)
app.use(router);
app.component('Highlight', Highlight);

app.mount('#app');
