<template>
    <div class="container">
        <div class="frame">
            <div class="padded">
                <label>Enter a text to highlight
                    <textarea v-model="input" class="homework"></textarea>
                </label>
            </div>
            <div class="homework">
                <label class="hw">
                    Highlight string:
                    <input v-model="highlight"
                    name="highlight"
                    autocomplete="off"
                    type="text"/>
                </label>
                <div class="colourChoice">
                    <label class="hw">
                        Highlighting color:
                        <input v-model="colourChoice"
                        name="colourChoice"
                        type="color">
                    </label>
                </div>
            </div>
            <h4>Highlight v1</h4>
            <span v-for="n in inputArrayLength" v-bind:key="n">
                <mark v-if="highlightedWord.includes(n)"> {{inputArray[n - 1]}} </mark>
                <span v-if="highlightedWord.includes(n) != true"> {{inputArray[n - 1]}} </span>
            </span>
            <div class="homework"> </div>
            <h4>Highlight v2</h4>
            <span v-for="n in inputArrayLength" v-bind:key="n">
                <span v-if="highlightedWord.includes(n)" class="highlight"> {{inputArray[n - 1]}} </span>
                <span v-if="highlightedWord.includes(n) != true"> {{inputArray[n - 1]}} </span>
            </span>
            <div class="homework"> </div>
            <h4>Highlight v3</h4>
            <span v-for="n in inputArrayLength" v-bind:key="n">
                <span v-if="highlightedWord.includes(n)" :style="{'background-color':colourChoice}"> {{inputArray[n - 1]}} </span>
                <span v-if="highlightedWord.includes(n) != true"> {{inputArray[n - 1]}} </span>
            </span>
            <div class="homework">
                    <span> </span>
            </div>
        </div>
    </div>
</template>
<style>

.container {
  display: flex;
  justify-content: center;
  padding:10px;
}
.colourChoice {
    padding:10px;
}
.padded {
    padding:10px;
    padding-left:30px;
}
span.highlight {
    background-color: coral;
}
span.highlight {
    background-color: coral;
}

textarea.homework{
    width: 80%;
}

div.homework{
    border-bottom: thin groove black;
    width: 80%;
    padding: 5px;
    margin: 5px;
    display: block;
    margin-left: 50px;
    margin-right: 50px;
}

.hw{
    height: 20px;
}

</style>
<script>
import { ref, computed } from 'vue';

export default {
  name: 'Highlighting',
  setup() {
    const input = ref('');
    const colourChoice = ref('#000000');
    const highlight = ref('');
    const inputArray = computed(() => input.value.split(''));
    const inputArrayLength = computed(() => inputArray.value.length + 1);

    const highlightedWord = computed(() => {
      const highlightSplit = highlight.value.split('');
      console.log(highlightSplit);
      let y = [];

      for (let i = 0; i < inputArray.value.length; i++) {
        const z = [];
        let matchCount = 0;
        console.log(y);
        for (let k = 0; k < highlightSplit.length; k++) {
          if (highlightSplit[k] == inputArray.value[i + k]) {
            z.push(i + k + 1);
            matchCount++;
          } else { break; }
          if (matchCount == highlightSplit.length) {
            y = y.concat(z);
          }
        }
      }
      return y;
    });

    return {
      input,
      colourChoice,
      highlight,
      inputArray,
      highlightedWord,
      inputArrayLength,
    };
  },
};
</script>
