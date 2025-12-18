param(
    [string]$Python = "python",
    [string]$Script = "parte-2.py"
)

$cases = @(
    "1;5;prueba-1;salida1",
    "1;6;prueba-2;salida2",
    "1;1;prueba-3;salida3",
    "1;30;prueba-4;salida4",
    "1;7;prueba-1;salida5",
    "1;4;prueba-6;salida6",
    "1;309;USA-road-d.BAY;salida7"
)

Write-Host "== Ejecutando pruebas =="

foreach ($row in $cases) {
    $parts = $row -split ';'
    $origen, $destino, $mapa, $salida = $parts

    Write-Host ""
    Write-Host "--------------------------------------------"
    Write-Host "Ejecutando: $origen -> $destino (mapa=$mapa)"
    Write-Host "--------------------------------------------"

    & $Python $Script $origen $destino $mapa $salida
}

Write-Host ""
Write-Host "OK: pruebas finalizadas."