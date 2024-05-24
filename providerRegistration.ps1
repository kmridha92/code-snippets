# Register providers for Azure subscription

Param(
    [Parameter(Mandatory)]
    [string]$SubscriptionID
)

Select-AzSubscription -SubscriptionId $SubscriptionID

$providers = @('Microsoft.PowerBI','Microsoft.PowerPlatform','Microsoft.PowerBIDedicated')

foreach ($provider in $providers ) {
  $iterationCount = 0
  $maxIterations = 30
  $providerStatus = (Get-AzResourceProvider -ListAvailable | Where-Object ProviderNamespace -eq $provider).registrationState
  if ($providerStatus -ne 'Registered') {
    Write-Output "`n Registering the '$provider' provider"
    Register-AzResourceProvider -ProviderNamespace $provider
    do {
      $providerStatus = (Get-AzResourceProvider -ListAvailable | Where-Object ProviderNamespace -eq $provider).registrationState
      $iterationCount++
      Write-Output "Waiting for the '$provider' provider registration to complete....waiting 10 seconds"
      Start-Sleep -Seconds 10
    } until ($providerStatus -eq 'Registered' -and $iterationCount -ne $maxIterations)
    if ($iterationCount -ne $maxIterations) {
      Write-Output "`n The '$provider' has been registered successfully"
    }
    else {
      Write-Output "`n The '$provider' has not been registered successfully"
    }
  }
}