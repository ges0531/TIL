<template>
    <div>
        <!-- method 는 내가 인자를 넘긴다면 (ARG) 붙이고 -->
        <!-- 그게 아니라면 () 안붙임 -->
        <!-- ()는 커스텀 인자 없으면 안붙임 -->
        <!-- v-on: 을 줄여서 @ -->
        <!-- <input @input="onInput" type="text"> -->
        <input @keypress.enter="onInput" type="text">
    </div>
</template>

<script>
export default {
    name: 'SearchBar',  // new comp: 0. 이름적기
    methods: {  // 할 행동들
        onInput (e) {
            // console.log(e.target.value);
            // e 가 발생했는데 그 이벤트에 대한 value
            // this.$emit('Event이름', 전송할 값): 자식component => 부모component 정보(데이터)를 올려보낼 때 
            this.$emit('inputChange', e.target.value)
        }
    },
}
</script>

<style scoped>
/* scoped: 해당 컴포넌트의 태그들만 영향알 받는다! */
    input {
        width: 75%;
    }

    div {
        text-align: center;
        margin: 20px;
    }
</style>