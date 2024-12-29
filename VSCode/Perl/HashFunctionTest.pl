sub PrintHash{
    my @array = @_;
    foreach my $value (@array){
        print "value: " . $value . "\n"
    }
}

%hash = ('name' => 'wxss', 'age' => '22');

PrintHash(%hash);