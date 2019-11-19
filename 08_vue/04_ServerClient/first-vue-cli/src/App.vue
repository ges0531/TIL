<template>
    <!-- 반드시, Templage 안에는 "단 1개" 의 최상단 태그(노드) -->
    <div>
        <!-- <h1>나쁜말 거름종이</h1>
        <input type="text" v-model="input">
        <p>{{ filteredInput }}</p> -->
        <div v-bind:style= "{ color: activeColor, fontSize: fontSize + 'px' }">
            HIHI
        </div>
        <div class="static" v-bind:class= "{ active: isActive, error: hasError }">
            Hi
        </div>
    </div>
</template>

<script>
export default {
    name: 'App',
    // 왜인지는 모르겠지만, 이제부터는 data 를 function 으로 만들어야 해..

    data: function () {
    return {
    activeColor: 'red',
    fontSize: 30,
    isActive: true,
    hasError: false
        }
    },
    // data: function () {
    //     return {
    //         input: '',
    //     }
    // },
    methods: {},
    computed: {
        filteredInput: function () {
            // [바보] 가 들어오면, ** 로 바꿔서 return 하도록 한다.
            return this.input.replace(/바보|멍청이|똥개/g, "#")
        }
    },
}
</script>

<style>

</style>