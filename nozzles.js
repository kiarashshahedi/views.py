document.getElementById('gasoline_nozzles').addEventListener('change', function() {
        var nozzleCount = parseInt(this.value);
        var container = document.getElementById('gasoline-nozzles');
        container.innerHTML = '';
        for (var i = 0; i < nozzleCount; i++) {
            container.innerHTML += `
                <div class="form-group">
                    <label for="gasoline_nozzle_start_totalizer_${i}">Start Totalizer for Nozzle ${i + 1}</label>
                    <input type="number" step="0.01" id="gasoline_nozzle_start_totalizer_${i}" name="gasoline_nozzle_start_totalizer_${i}" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="gasoline_nozzle_end_totalizer_${i}">End Totalizer for Nozzle ${i + 1}</label>
                    <input type="number" step="0.01" id="gasoline_nozzle_end_totalizer_${i}" name="gasoline_nozzle_end_totalizer_${i}" class="form-control" required>
                </div>
            `;
        }
    });

    document.getElementById('gas_nozzles').addEventListener('change', function() {
        var nozzleCount = parseInt(this.value);
        var container = document.getElementById('gas-nozzles');
        container.innerHTML = '';
        for (var i = 0; i < nozzleCount; i++) {
            container.innerHTML += `
                <div class="form-group">
                    <label for="gas_nozzle_start_totalizer_${i}">Start Totalizer for Nozzle ${i + 1}</label>
                    <input type="number" step="0.01" id="gas_nozzle_start_totalizer_${i}" name="gas_nozzle_start_totalizer_${i}" class="form-control" required>
                </div>
                <div class="form-group">
                    <label for="gas_nozzle_end_totalizer_${i}">End Totalizer for Nozzle ${i + 1}</label>
                    <input type="number" step="0.01" id="gas_nozzle_end_totalizer_${i}" name="gas_nozzle_end_totalizer_${i}" class="form-control" required>
                </div>
            `;
        }
    });
</script>
