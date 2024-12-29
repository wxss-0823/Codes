$dir = "D:/*";
my @files = glob($dir);
foreach (@files){
    print $_ . "\n";
}
