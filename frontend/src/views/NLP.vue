<template>


<head>
    <meta charset="UTF-8">
    <title>About</title>
</head>
<body class="frame">
<h1>NLP Parser</h1>

<div>
    <textarea rows="3" v-model="input" class="input_form"></textarea>
</div>
<div class="button_row">

    <form class="nlp_form" @submit.prevent="postPOSConfirm()">
        <button class="nlp_button" type="submit">Display Parts of Speech </button>
    </form>

    <form class="nlp_form" @submit.prevent="postENTConfirm()">
        <button class="nlp_button" type="submit">Display Named Entities</button>
    </form>
</div>
<div class="highlight_form">
    <button class="highlight_button" v-on:click="highlighting = !highlighting">Highlight</button>
</div>
<br>
<h3>Results</h3>
<div class="">
    <div class="output_row">
        <Highlight v-for="n in outputLength" :newCol=newCol @colChange="updateColours" :output=output :nlpData=nlp_data :highlighting=highlighting :index="n" :key="n"> </Highlight>
    </div>
</div>

</body>


</template>
<style>
.frame{
    text-align: center;
}
.button_row{
    display:flex;
    text-align: center;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    }

.container{
    width:800px;
    border: 1px solid red;
    position: fixed;
    left: 50%;
    transform: translate(-50%, 0);
}
.output_row{
    display:flex;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    }

.nlp_form{
    padding:5px;
}
.input_form{
    width:385px;
    padding:2px;
}
.highlight_form{
    padding:10px;
    font-size:medium;
}
.nlp_button{
    color:white;
    background-color:#4CAF50;
}
.highlight_button{
    color:black;
    background-color:white;
    transition-duration: 0.225s;
}
.highlight_button:hover {
    color:white;
    background-color:#feed01;
}
</style>
<script>
import { ref, computed, watch } from 'vue';
import axios from 'axios';

export default {
  name: 'NLP',
  setup({emit}) {

    const nlp_data = ref([]);
    const input = ref('');
    const output = ref('');
    const newCol = ref([]);
    const outputLength = ref('');
    const highlighting = ref(false);
    console.log('main change')

    const updateColours = (val) => {
        newCol.value = val;
        console.log('got emittttttttttttttttttta');
    }

    const getPOSResponse = () => {
        const path = 'http://localhost:5000/pos';
        axios.get(path)
        .then((res) => {
            nlp_data.value = (JSON.parse(res.data));
            output.value = nlp_data.value.map(item => { return item.text });
            outputLength.value = output.value.length;
            console.log('output length pos' + outputLength.value);

            console.log('POS OUTPUT ' + nlp_data.value);

        })

        .catch((error) => {
            console.error(error);
        });
    }
    const postPOS = () => {
        highlighting.value = false;
        const path = 'http://localhost:5000/pos';
        var payload = {'input':input.value};
        console.log('POS INPUT ' + payload);
        axios.post(path, payload)
        .then(() => {
            getPOSResponse()
                })
        .catch((error) => {
            console.error(error);
        });
    }


    const getENTResponse = () => {
        const path = 'http://localhost:5000/ner';
        axios.get(path)
        .then((res) => {
            nlp_data.value = (JSON.parse(res.data));
            console.log('before input change ' + input.value)
            output.value = input.value.split(/[\s,.]+/);
            console.log('after input change ' + input.value)
            console.log('output length b4 ent' + outputLength.value);

            outputLength.value = output.value.length;
            console.log('output length ent' + outputLength.value);


            console.log('ENT OUTPUT ' + nlp_data.value);

        })

        .catch((error) => {
            console.error(error);
        });
    }
    const postENT = () => {
        highlighting.value = false;
        const path = 'http://localhost:5000/ner';
        var payload = {'input':input.value};
        console.log('ENT INPUT ' + payload);
        axios.post(path, payload)
        .then(() => {
            getENTResponse()
                })
        .catch((error) => {
            console.error(error);
        });
    }
    const postENTConfirm = () => {
        postENT()
        postENT()
    }
    const postPOSConfirm = () => {
        postPOS()
        postPOS()
    }

    return {
      nlp_data,
      postPOS,
      postENT,
      postPOSConfirm,
      postENTConfirm,
      updateColours,
      input,
      output,
      outputLength,
      highlighting,
      newCol,
    };
  },
};
</script>

