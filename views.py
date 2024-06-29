def create_station(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        gasoline_tanks = int(request.POST.get('gasoline_tanks'))
        gasoline_nozzles = int(request.POST.get('gasoline_nozzles'))
        gas_nozzles = int(request.POST.get('gas_nozzles'))
        gas_tanks = int(request.POST.get('gas_tanks'))
        gasoline_beginning = float(request.POST.get('gasoline_beginning'))
        gas_beginning = float(request.POST.get('gas_beginning'))
        gasoline_received = float(request.POST.get('gasoline_received'))
        gas_received = float(request.POST.get('gas_received'))
        electronic_gasoline_sales = float(request.POST.get('electronic_gasoline_sales'))
        electronic_gas_sales = float(request.POST.get('electronic_gas_sales'))
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        station = FuelStation.objects.create(
            name=name,
            gasoline_tanks=gasoline_tanks,
            gas_tanks=gas_tanks,
            gasoline_nozzles=gasoline_nozzles,
            gas_nozzles=gas_nozzles,
            gasoline_beginning=gasoline_beginning,
            gas_beginning=gas_beginning,
            gasoline_received=gasoline_received,
            gas_received=gas_received,
            electronic_gasoline_sales=electronic_gasoline_sales,
            electronic_gas_sales=electronic_gas_sales,
            start_date=start_date,
            end_date=end_date
        )
        
        for i in range(gasoline_tanks):
            amount = float(request.POST.get(f'gasoline_tank_{i}'))
            Tank.objects.create(station=station, type='gasoline', amount=amount)
        for i in range(gas_tanks):
            amount = float(request.POST.get(f'gas_tank_{i}'))
            Tank.objects.create(station=station, type='gas', amount=amount)

        for i in range(gasoline_nozzles):
            start_totalizer = float(request.POST.get(f'gasoline_nozzle_start_totalizer_{i}'))
            end_totalizer = float(request.POST.get(f'gasoline_nozzle_end_totalizer_{i}'))
            Nozzle.objects.create(station=station, type='gasoline', start_totalizer=start_totalizer, end_totalizer=end_totalizer)
        for i in range(gas_nozzles):
            start_totalizer = float(request.POST.get(f'gas_nozzle_start_totalizer_{i}'))
            end_totalizer = float(request.POST.get(f'gas_nozzle_end_totalizer_{i}'))
            Nozzle.objects.create(station=station, type='gas', start_totalizer=start_totalizer, end_totalizer=end_totalizer)
        return render(request, 'create_station.html', {'station': station, 'success': True})
    
    return render(request, 'create_station.html')
