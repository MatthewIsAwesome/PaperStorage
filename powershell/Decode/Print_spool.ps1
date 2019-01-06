param(

[Parameter(mandatory = $true)]
[int32]$mode,

[Parameter(mandatory = $false)]
[int32]$confirm

)

$usage = '




'


$defaultprint = Get-WmiObject -Query " SELECT * FROM Win32_Printer WHERE Default=$true"
$printname = $defaultprint.ShareName
$printname | Set-PrintConfiguration -DuplexingMode TwoSidedLongEdge

echo "Found $($printname) as default printer"
if($confirm -ne 1){throw 'Exiting to continue set the flag -confirm to 1'}
 