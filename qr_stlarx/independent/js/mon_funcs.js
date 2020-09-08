function jq_toghidden(id) {
    if ( $( "#" + id ).is( ":hidden" ) ) {
        $( "#" + id ).slideDown(  );
    } else {
        $( "#" + id ).slideUp();
    }
}
