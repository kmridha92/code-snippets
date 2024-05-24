# Copy secrets from one KeyVault to another

Param(
    [Parameter(Mandatory)]
    [string]$sourceVaultName,
    [Parameter(Mandatory)]
    [string]$destVaultName
)

Connect-AzAccount

$secretNames = (Get-AzKeyVaultSecret -VaultName $sourceVaultName).Name
$secretNames.foreach{
    Set-AzKeyVaultSecret -VaultName $destVaultName -Name $_ `
        -SecretValue (Get-AzKeyVaultSecret -VaultName $sourceVaultName -Name $_).SecretValue
}