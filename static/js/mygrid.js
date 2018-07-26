<script>
    
    var clients = [
        { "Serial": "Otto Clay", "Articulo": 25, "Entrada": 1, "Salida": "Ap #897-1459 Quam Avenue", "Descripción": false }
    ];
 
    // var countries = [
    //     { Name: "", Id: 0 },
    //     { Name: "United States", Id: 1 },
    //     { Name: "Canada", Id: 2 },
    //     { Name: "United Kingdom", Id: 3 }
    // ];
 
    $("#jsGrid").jsGrid({
        width: "100%",
        height: "400px",
 
        inserting: true,
        editing: true,
        sorting: true,
        paging: true,
 
        data: clients,
 
        fields: [
            { name: "Serial", type: "text", width: 150, validate: "required" },
            { name: "Artículo", type: "number", width: 50 },
            { name: "Entrada", type: "text", width: 200 },
            { name: "Salida", type: "text", textField: "S" },
            { name: "Descripción", type: "text", sorting: false },
            { type: "control" }
        ]
    });
</script>