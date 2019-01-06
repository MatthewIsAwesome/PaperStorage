param(



)

$defaultprint = Get-WmiObject -Query " SELECT * FROM Win32_Printer WHERE Default=$true"
$printname = $defaultprint.ShareName
$printname | Set-PrintConfiguration -DuplexingMode TwoSidedLongEdge

echo "Found $($printname) as default printer"
echo 