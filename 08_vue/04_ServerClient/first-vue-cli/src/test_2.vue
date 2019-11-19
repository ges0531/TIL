<template>
    <div v-bind:style= "{ color: activeColor, fontSize: fontSize + 'px' }">
        HIHI
    </div>
</template>

<script>
export default {
    data: function () {
        return {
        activeColor: 'red',
        fontSize: 30
        }
    },
}
</script>