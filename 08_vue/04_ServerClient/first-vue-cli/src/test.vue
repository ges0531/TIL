<template>
    <div class="static" v-bind:class= "{ active: isActive, error: hasError }">
        Hi
    </div>
</template>

<script>
export default {
    data: function () {
        return {
        isActive: true,
        hasError: false
        }
    },
}
</script>