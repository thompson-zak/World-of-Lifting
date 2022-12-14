<template>
  <b-navbar type="dark" variant="light">
        <b-navbar-brand href="#">World of Lifting</b-navbar-brand>
  </b-navbar>
  <PowerliftingForm />
</template>

<script>
import PowerliftingForm from './PowerliftingForm.vue';

export default {
  components: {
    PowerliftingForm,
  },
};
</script>
