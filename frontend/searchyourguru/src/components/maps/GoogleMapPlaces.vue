<template>
                <vue-google-autocomplete
                    id="tution_area"
                    classname="input"
                    placeholder="eg: 110092 or Laxmi Nagar or Delhi"
                    v-on:placechanged="getAddress"
                    country="in"
                >
                </vue-google-autocomplete>
</template>


<script>
import VueGoogleAutocomplete from 'vue-google-autocomplete'

export default {
    name: 'GoogleMapPlaces',
    methods: {
        getAddress: function(addressData, placeData, id) {
            console.log(addressData);
            console.log(placeData);
            console.log(id);
        }
    },
    components: { VueGoogleAutocomplete }
}
</script>