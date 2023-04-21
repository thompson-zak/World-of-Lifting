<template>
  <b-container fluid class="powerliftingPageContainer">

    <b-row align-v="center" class="powerliftingPageRow" v-if="displayResults">

      <b-col align-self="start" cols=1>
        <HomeButton/>
      </b-col>

      <b-col cols=10>
        <PowerliftingResults :liftData="liftData"/>

        <div v-if="displaySpinner">
          <b-spinner label="Spinning"></b-spinner>
        </div>
      </b-col>

      <b-col cols=1>
        <HomeButton/>
      </b-col>

    </b-row>

    <b-row align-v="center" class="powerliftingPageRow" v-else>

      <b-col align-self="start" cols=1>
        <HomeButton/>
      </b-col>

      <b-col cols=12>
        <PowerliftingForm
          @requestSubmitted="onFormSubmit"
          @analyzeLiftsData="onFormReturn"
          v-show="displayForm"
        />
      </b-col>

      <b-col cols=1></b-col>

    </b-row>

  </b-container>
</template>

<script>
import PowerliftingForm from './PowerliftingForm.vue';
import PowerliftingResults from './PowerliftingResults.vue';
import HomeButton from '../HomeButton.vue';

export default {
  name: 'PowerliftingHomePage',
  components: {
    PowerliftingForm,
    PowerliftingResults,
    HomeButton,
  },
  data() {
    return {
      displayResults: false,
      displayForm: true,
      displaySpinner: false,
      liftData: {},
    };
  },
  methods: {
    onFormSubmit() {
      this.displayResults = false;
      this.displaySpinner = true;
    },
    onFormReturn(data) {
      // This is where you will update everything with emitted data
      this.liftData = data;
      this.displaySpinner = false;
      this.displayResults = true;
    },
  },
};
</script>
