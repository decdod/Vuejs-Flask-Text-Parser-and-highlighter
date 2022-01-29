<template>
<div class="highlight">
    <div class="pos"> {{pos}} </div>
    <span class="text" v-on:click="clicked = !clicked" :style="{'background-color':displayed_colour}">  {{text}}  </span>
    <div>
    <input type="color" v-model="colourChange" v-if="clicked == true && highlighting == true">
    </div>
</div>
</template>
<script>
import {onUpdated, ref, watch} from 'vue';
console.log('asd')

export default {
    props: {
        index:Number,
        nlpData: Array,
        output: Array,
        highlighting: Boolean,
        newCol: Array,
    },
    setup(props, {emit}) {
        const text = ref('');
        const pos = ref('');
        const clicked = ref('');
        const displayed_colour = ref('transparent');
        const colour = ref('transparent');
        const colourChange = ref(displayed_colour);
        var newColour = 'transparent';
        const toBeColoured = ref(false);
        const tags = ["PRON", "CCONJ", "PART", "ADV", "INTJ", "SCONJ", "ADP", "DET", "NOUN", "PUNCT", "VERB", "ADJ", "PROPN", "AUX", "SYM", "NUM", "LOC", "NORP", "GPE", "ORDINAL", "DATE", "PERSON", "ORG", "CARDINAL"]
        const tagGroups = ref({'PRON':'transparent', 'CCONJ':'transparent', 'PART':'transparent', 'ADV':'transparent', 'INTJ':'transparent', 'SCONJ':'transparent', 'ADP':'transparent', 'DET':'transparent', 'NOUN':'transparent', 'PUNCT':'transparent', 'VERB':'transparent', 'ADJ':'transparent', 'PROPN':'transparent', 'AUX':'transparent', 'SYM':'transparent',
        'NUM':'transparent', 'LOC':'transparent', 'NORP':'transparent', 'GPE':'transparent', 'ORDINAL':'transparent' , 'DATE':'transparent' , 'PERSON':'transparent' , 'ORG':'transparent', 'CARDINAL':'transparent'});
        const colours = ['#86aff9', '#eda1bd', '#fff293', '#49edda', '#b282e0', '#6be092', '#e55e6d', '#f9c775', '#b8fc79', '#f9817f', '#86aff9', '#eda1bd', '#fff293', '#49edda', '#b282e0', '#6be092',
        '#e55e6d', '#f9c775', '#b8fc79', '#f9817f', '#86aff9', '#eda1bd', '#fff293', '#49edda', '#b282e0', '#6be092', '#e55e6d', '#f9c775', '#b8fc79', '#f9817f', '#86aff9', '#eda1bd', '#fff293', '#49edda', '#b282e0', '#6be092', '#e55e6d', '#f9c775', '#b8fc79', '#f9817f', '#86aff9']
        console.log(props.nlpData);


        if (props.nlpData.length > 0) {

            if('pos' in props.nlpData[0]){
                if (props.nlpData.length > 0) {
                    console.log('pos grande');
                    text.value = props.nlpData[props.index - 1].text;
                    console.log(text.value);
                    pos.value = props.nlpData[props.index - 1].pos;
                    toBeColoured.value = true;

                }

                watch(() => props.nlpData, () => {
                    if (props.nlpData.length > 0) {
                        if('pos' in props.nlpData[0]) {
                            console.log('pos update');
                            text.value = props.nlpData[props.index - 1].text;
                            console.log(text.value);
                            pos.value = props.nlpData[props.index - 1].pos;
                            toBeColoured.value = true

                        }
                    }
                    if(toBeColoured.value == true) {
                        if (tagGroups.value[pos.value] != 'transparent'){
                            newColour = tagGroups.value[pos.value];
                        }
                        else{
                            tagGroups.value[pos.value] = colours[tags.findIndex(function(tag){return tag == pos.value})]; // finds index of tag and assigns matching index colour in array
                            newColour = tagGroups.value[pos.value];
                        }
                        colour.value = newColour
                    }
                    else{
                        colour.value = 'transparent';
                        newColour = 'transparent';
                    }
                    toBeColoured.value = false

                })
            }
            else{
                if (props.nlpData.length > 0) {
                    console.log('ent grande');
                    text.value = props.output[props.index - 1];
                    console.log(props.output);
                    console.log(props.index - 1);

                    console.log(text.value);
                    pos.value = '';
                    for (var i = 0; i < props.nlpData.length; i++) {
                        if (props.output[props.index - 1] == props.nlpData[i].text){
                            toBeColoured.value = true
                            pos.value = props.nlpData[i].ne_label;
                            console.log('ent found colour change ');
                        }

                    }


                }

                watch(() => props.nlpData, () => {
                    if (props.nlpData.length > 0) {
                        if('ne_label' in props.nlpData[0]) {
                            console.log('ent update');
                            text.value = props.output[props.index - 1];
                            console.log('index - 1 ');
                            console.log(props.index - 1);
                            console.log(text.value);
                            pos.value = '';
                            for (var i = 0; i < props.nlpData.length; i++) {
                                if (props.output[props.index - 1] == props.nlpData[i].text){
                                    toBeColoured.value = true
                                    pos.value = props.nlpData[i].ne_label;

                                }

                            }
                        }

                    if(toBeColoured.value == true) {
                        if (tagGroups.value[pos.value] != 'transparent'){
                            newColour = tagGroups.value[pos.value];
                        }
                        else{
                            tagGroups.value[pos.value] = colours[tags.findIndex(function(tag){return tag == pos.value})]; // finds index of tag and assigns matching index colour in array
                            newColour = tagGroups.value[pos.value];
                        }
                        colour.value = newColour;
                    }
                    else{
                        colour.value = 'transparent';
                        newColour = 'transparent';
                    }
                    toBeColoured.value = false;
                    }
                })
            }
        }
        else {
            text.value = props.output[props.index - 1];
            toBeColoured.value = false;
            newColour = 'transparent';

        }
        if(toBeColoured.value == true) {
            if (tagGroups.value[pos.value] != 'transparent'){
                newColour = tagGroups.value[pos.value];
            }
            else{
                tagGroups.value[pos.value] = colours[tags.findIndex(function(tag){return tag == pos.value})]; // finds index of tag and assigns matching index colour in array
                newColour = tagGroups.value[pos.value];
            }
            colour.value = newColour
        }
        else{
            colour.value = 'transparent';
            newColour = 'transparent';
        }
        toBeColoured.value = false



        watch(() => props.output, () => {
            text.value = '';
            pos.value = '';
            colour.value = 'transparent';
            newColour = 'transparent';
            if (props.nlpData.length > 0) {

                if('pos' in props.nlpData[0]){
                    if (props.nlpData.length > 0) {
                        console.log('pos grande');
                        text.value = props.nlpData[props.index - 1].text;
                        console.log(text.value);
                        pos.value = props.nlpData[props.index - 1].pos;
                        toBeColoured.value = true

                    }

                    watch(() => props.nlpData, () => {
                        if (props.nlpData.length > 0) {
                            if('pos' in props.nlpData[0]) {
                                console.log('pos update');
                                text.value = props.nlpData[props.index - 1].text;
                                console.log(text.value);
                                pos.value = props.nlpData[props.index - 1].pos;
                                toBeColoured.value = true
                            }
                        }
                    })
                }
                else{
                    if (props.nlpData.length > 0) {
                        console.log('ent grande');
                        text.value = props.output[props.index - 1];
                        console.log(props.output);
                        console.log(props.index - 1);

                        console.log(text.value);
                        pos.value = '';
                        toBeColoured.value = false

                        for (var i = 0; i < props.nlpData.length; i++) {
                            if (props.output[props.index - 1] == props.nlpData[i].text){
                                pos.value = props.nlpData[i].ne_label;
                                toBeColoured.value = true

                            }

                        }
                        if(toBeColoured.value == true) {
                            if (tagGroups.value[pos.value] != 'transparent'){
                                newColour = tagGroups.value[pos.value];
                            }
                            else{
                                tagGroups.value[pos.value] = colours[tags.findIndex(function(tag){return tag == pos.value})]; // finds index of tag and assigns matching index colour in array
                                newColour = tagGroups.value[pos.value];
                            }
                            colour.value = newColour
                        }
                        else{
                            colour.value = 'transparent';
                            newColour = 'transparent';

                        }
                        toBeColoured.value = false


                    }

                    watch(() => props.nlpData, () => {
                        if (props.nlpData.length > 0) {
                            if('ne_label' in props.nlpData[0]) {
                                console.log('ent update');
                                text.value = props.output[props.index - 1];
                                console.log('index - 1 ');
                                console.log(props.index - 1);
                                console.log(text.value);
                                pos.value = '';
                                toBeColoured.value = false
                                for (var i = 0; i < props.nlpData.length; i++) {
                                    if (props.output[props.index - 1] == props.nlpData[i].text){
                                        pos.value = props.nlpData[i].ne_label;
                                        toBeColoured.value = true
                                    }

                                }
                                if(toBeColoured.value == true) {
                                    if (tagGroups.value[pos.value] != 'transparent'){
                                        newColour = tagGroups.value[pos.value];
                                    }
                                    else{
                                        tagGroups.value[pos.value] = colours[tags.findIndex(function(tag){return tag == pos.value})]; // finds index of tag and assigns matching index colour in array
                                        newColour = tagGroups.value[pos.value];
                                    }
                                    colour.value = newColour;
                                }
                                else{
                                    colour.value = 'transparent'
                                    newColour = 'transparent';
                                }
                                toBeColoured.value = false

                            }
                        }
                    })
                }
            }
            else {
                text.value = props.output[props.index - 1];
                toBeColoured.value = false
            }
            if(toBeColoured.value == true) {
                if (tagGroups.value[pos.value] != 'transparent'){
                    newColour = tagGroups.value[pos.value];
                }
                else{
                    tagGroups.value[pos.value] = colours[tags.findIndex(function(tag){return tag == pos.value})]; // finds index of tag and assigns matching index colour in array
                    newColour = tagGroups.value[pos.value];
                }
                colour.value = newColour;
            }
            else{
                colour.value = 'transparent';
                newColour = 'transparent';
            }
            toBeColoured.value = false;


        })

        watch(() => props.highlighting, () => {
            if(props.highlighting == true){
            displayed_colour.value = colour.value;
            }
            else{
            displayed_colour.value = 'transparent';
            }
        })
        watch(() => colourChange.value, () => {
            emit('colChange', [pos.value, colourChange.value]);
        })

        watch(() => props.newCol, () => {
            console.log('old');
            console.log(props.newCol);
            if(props.newCol[0] == pos.value){
                displayed_colour.value = props.newCol[1]
            }
            console.log(props.newCol)
            console.log(text.value)


        })

        return{
            text,
            pos,
            colour,
            toBeColoured,
            colourChange,
            tagGroups,
            clicked,
            displayed_colour,
        }

    },
    name: 'Highlight'

}
</script>
<style>
.highlight{
    margin-right: 10px;
}
.pos{
    font-size: small;

}
.text{
    font-size: large;
}

</style>