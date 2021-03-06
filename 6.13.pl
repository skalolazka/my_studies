#!/usr/bin/perl

# rotate array by i positions

use strict;
use warnings;

package MyRotate;

sub new {
    return bless {} => shift;
}

sub reverse {
    my ($self, $arr, $start, $end) = @_;
    return if (!scalar(@$arr) || $start >= $end || $end > scalar(@$arr));
    for (my $j = $start, my $rj = $end-1; $j < $rj; $j++, $rj--) {
        ($arr->[$j], $arr->[$rj]) = ($arr->[$rj], $arr->[$j]);
    }
}

sub rotate1 { # previous version, was tested before
    my ($self, $arr, $i) = @_;
    $self->reverse($arr, 0, $i);
    $self->reverse($arr, $i, scalar(@$arr));
    $self->reverse($arr, 0, scalar(@$arr));
}

sub rotate {
    my ($self, $arr, $i, $start, $end) = @_;
    ($start, $end) = (0, scalar(@$arr)) unless (defined($start));
    $i %= scalar(@$arr);
    return if (!scalar(@$arr) || !$i);
    while ($start < $end && $i < $end - $start) {
        if ($i <= int(($end - $start) / 2)) {
            $self->swap($arr, $start, $start + $i, $end - $i);
            $end -= $i;
        }
        else {
            $self->swap($arr, $start, $end - $i, $start + $i);
            my $old_i = $i;
            $i = $start - $end + 2 * $i;
            $start = $end - $old_i;
        }
    }
}

sub swap {
    my ($self, $arr, $start1, $end1, $start2) = @_;
    for (my $i = $start1, my $j = $start2; $i < $end1; $i++, $j++) {
        ($arr->[$i], $arr->[$j]) = ($arr->[$j], $arr->[$i]);
    }
}

package TestMyRotate;
use Test::More;
use Test::Deep;

my $module = MyRotate->new;

my $swap = [];
$module->swap($swap, 0, 0, 0);
is_deeply($swap, [], 'swap empty');
$swap = [0,1,2,3,4,5,6,7,8];
$module->swap($swap, 0, 0, 0);
is_deeply($swap, [0,1,2,3,4,5,6,7,8], 'swap none');
$module->swap($swap, 0, 0, 9);
is_deeply($swap, [0,1,2,3,4,5,6,7,8], 'swap none again');
$module->swap($swap, 0, 1, 8);
is_deeply($swap, [8,1,2,3,4,5,6,7,0], 'swap one');
$module->swap($swap, 0, 1, 1);
is_deeply($swap, [1,8,2,3,4,5,6,7,0], 'swap one in start');
$module->swap($swap, 3, 4, 4);
is_deeply($swap, [1,8,2,4,3,5,6,7,0], 'swap one in middle');
$module->swap($swap, 0, 3, 4);
is_deeply($swap, [3,5,6,4,1,8,2,7,0], 'swap three in start');
$module->swap($swap, 3, 6, 6);
is_deeply($swap, [3,5,6,2,7,0,4,1,8], 'swap three in middle');

my $test = [];
$module->reverse($test, 0, scalar(@$test));
is_deeply($test, [], 'zero reverse OK');
$test = [1];
$module->reverse($test, 0, scalar(@$test));
is_deeply($test, [1], '1 elem reverse OK');
$test = [1,2,3,4,5];
$module->reverse($test, 0, scalar(@$test));
is_deeply($test, [5,4,3,2,1], 'full reverse OK');
$module->reverse($test, 0, 0);
is_deeply($test, [5,4,3,2,1], 'no reverse');
$module->reverse($test, 0, 1);
is_deeply($test, [5,4,3,2,1], 'no reverse');
$module->reverse($test, 0, 2);
is_deeply($test, [4,5,3,2,1], '2 first elem reverse');
$test = [1,2,3,4,5,6,7,8];
$module->reverse($test, 2, 5);
is_deeply($test, [1,2,5,4,3,6,7,8], 'reverse middle part');

my @test_data = (
    { in => [0], i => 0, out => [0] },
    { in => [0], i => 10, out => [0] }, # I actually assume i can't be > scalar(@$array)
    { in => [1, 0], i => 1, out => [0, 1]},
    { in => [0, 1, 2, 3], i => 1, out => [1, 2, 3, 0]},
    { in => [0, 1, 2, 3], i => 2, out => [2, 3, 0, 1]}, 
    { in => [0, 1, 2, 3], i => -1, out => [3, 0, 1, 2]}, 
    { in => [0, 1, 2, 3], i => 9, out => [1, 2, 3, 0]}, 
    { in => [0, 1, 2, 3], i => -9, out => [3, 0, 1, 2]}, 
    { in => [0, 1, 2, 3, 4], i => 2, out => [2, 3, 4, 0, 1]}, 
    { in => [0, 1, 2, 3, 4], i => 4, out => [4, 0, 1, 2, 3]},
    { in => [0, 1, 2, 3, 4], i => 5, out => [0, 1, 2, 3, 4]},
    { in => [0, 1, 2, 3, 4, 5], i => 2, out => [2, 3, 4, 5, 0, 1]},
);
for my $data (@test_data) {
    my $str = join(',', @{$data->{in}});
    $module->rotate($data->{in}, $data->{i});
    is_deeply($data->{in}, $data->{out}, "$str by $data->{i} OK");
}

done_testing;
